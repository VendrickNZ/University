import * as conversations from '../models/conversation.server.model';
import * as schemas from '../resources/schemas.json'
import Logger from '../../config/logger';
import {Request, Response} from 'express';
import {validate} from "../resources/validate";

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
    return null;
}

const read = async (req: Request, res: Response): Promise<void> => {
    return null;
}

const update = async (req: Request, res: Response): Promise<void> => {
    return null;
}

const remove = async (req: Request, res: Response): Promise<void> => {
    return null;
}

export { list, create, read, update, remove }