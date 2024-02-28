import * as conversations from '../models/conversation.server.model';
import * as schemas from '../resources/schemas.json'
import Logger from '../../config/logger';
import {Request, Response} from 'express';
import {validate} from "../resources/validate";
import * as users from "../models/user.server.model";

const list = async (req: Request, res: Response): Promise<void> => {
    Logger.http('GET all conversations')
    try {
        const result = await conversations.getAll();
        res.status(200).send(result);
    } catch (err) {
        res.status(500)
            .send(`ERROR getting users ${err}`);
    }
}

const create = async (req: Request, res: Response): Promise<void> => {
    Logger.http(`POST all conversations with ${req.body.convo_name}`)
    const validation = await validate(
        schemas.conversation,
        req.body);
    if (validation !== true) {
        res.statusMessage = `Bad Request: ${validation.toString()}`;
        res.status(400).send();
        return;
    }

    const convoName = req.body.convo_name;
    try {
        const result = await conversations.insert(convoName);
        res.status(201).send({"convo_id": result.insertId});
    } catch (err) {
        res.status(500).send(`ERROR creating conversation ${convoName}: ${err}`);
    }
}

const read = async (req: Request, res: Response): Promise<void> => {
    Logger.http(`GET single conversation id ${req.params.id}`)
    const id = req.params.id;
    try {
        const result = await conversations.getOne(parseInt(id, 10));
        if (result.length === 0) {
            res.status(404).send('Conversation not found');
        } else {
            res.status(200).send(result[0]);
        }
    } catch (err) {
        res.status(500).send(`ERROR reading conversation ${id}: ${err}`);
    }
}

const update = async (req: Request, res: Response): Promise<void> => {
    Logger.http(`ALTER single conversation id: ${req.params.id}`)
    const id = req.params.id;

    const validation = await validate(
        schemas.conversation,
        req.body);
    if (validation !== true) {
        res.statusMessage = `Invalid input: ${validation.toString()}`;
        res.status(400).send();
        return;
    }

    const convoName = req.body.convo_name;
    try {
        const conversation = await conversations.getOne(parseInt(id, 10));
        if (conversation.length === 0) {
            res.status(404).send('Conversation not found');
            return;
        }

        const result = await conversations.alter(parseInt(id, 10), convoName);
        res.status(200).send({"convo_id": result.insertId});

    } catch (err) {
        res.status(500).send(`ERROR updating conversation ${convoName}: ${err}`);
    }
}

const remove = async (req: Request, res: Response): Promise<void> => {
    Logger.http(`REMOVE single conversation id: ${req.params.id}`)
    const id = req.params.id;

    try {
        const conversation = await conversations.getOne(parseInt(id, 10));
        if (conversation.length === 0) {
            res.status(404).send('Conversation not found');
            return;
        }
        const result = await conversations.remove(parseInt(id, 10));
        res.status(200).send(`Conversation with ID ${id} deleted`);
    } catch (err) {
        res.status(500).send(`ERROR removing conversation with ID ${id}: ${err}`);
    }
}

export { list, create, read, update, remove }