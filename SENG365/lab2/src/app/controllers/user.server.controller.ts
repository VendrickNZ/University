import * as users from '../models/user.server.model';
import * as schemas from '../resources/schemas.json'
import Logger from '../../config/logger';
import {Request, Response} from 'express';

const list = async (req: Request, res: Response): Promise<void> => {
    Logger.http('GET all users')
    try {
        const result = await users.getAll();
        res.status(200).send(result);
    } catch (err) {
        res.status(500)
            .send(`ERROR getting users ${err}`);
    }
};

const create = async (req: Request, res: Response): Promise<void> => {
    Logger.http(`POST create a user with username: ${req.body.username}`)
    if (! req.body.hasOwnProperty("username")) {
        res.status(400).send("Please provide username field");
        return
    }
    const username = req.body.username;
    try {
        const result = await users.insert(username);
        res.status(201).send({"user_id": result.insertId});
    } catch (err) {
        res.status(500).send(`ERROR creating user ${username}: ${err}`);
    }
};

const read = async (req: Request, res: Response): Promise<void> => {
    Logger.http(`GET single user id: ${req.params.id}`)
    const id = req.params.id;
    try {
        const result = await users.getOne(parseInt(id, 10));
        if (result.length === 0){
            res.status(404).send('User not found');
        } else {
            res.status(200).send(result[0]);
        }
    } catch (err) {
        res.status(500).send(`ERROR reading user ${id}: ${err}`);
    }
};

const update = async (req: Request, res: Response): Promise<void> => {
    return null;
}

const remove = async (req: Request, res: Response): Promise<void> => {
    return null;
}

export {list, create, read, update, remove}