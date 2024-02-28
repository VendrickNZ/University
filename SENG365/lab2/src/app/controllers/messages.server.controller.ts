import * as messages from '../models/messages.server.model';
import * as schemas from '../resources/schemas.json'
import Logger from '../../config/logger';
import {Request, Response} from 'express';
import {validate} from "../resources/validate";
import * as users from "../models/user.server.model";

const list = async (req: Request, res: Response): Promise<void> => {
    Logger.http('GET all messages')
    try {
        const result = await messages.getAll();
        res.status(200).send(result);
    } catch (err) {
        res.status(500)
            .send(`ERROR getting messages ${err}`);
    }
}

const create = async (req: Request, res: Response): Promise<void> => {
    Logger.http(`POST create a message with message: ${req.body.message}`)
    const validation = await validate(
        schemas.message_creation,
        req.body);
    if (validation !== true) {
        res.statusMessage = `Bad Request: ${validation.toString()}`;
        res.status(400).send();
        return;
    }

    const { message, convo_id, user_id } = req.body;
    try {
        const result = await messages.insert(message, convo_id, user_id);
        res.status(201).send({"message_id": result.insertId});
    } catch (err) {
        res.status(500).send(`ERROR creating user ${message}: ${err}`);
    }
}

const read = async (req: Request, res: Response): Promise<void> => {
    Logger.http(`GET single message id: ${req.params.id}`)
    const id = req.params.id;
    try {
        const result = await messages.getOne(parseInt(id, 10));
        if (result.length === 0) {
            res.status(404).send('Message not found');
        } else {
            res.status(200).send(result[0]);
        }
    } catch (err) {
        res.status(500).send(`ERROR reading message ${id}: ${err}`)
    }
}

export { list, create, read }