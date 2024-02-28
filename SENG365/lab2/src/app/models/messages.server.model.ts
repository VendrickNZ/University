import {getPool} from '../../config/db';
import Logger from '../../config/logger';
import { ResultSetHeader} from "mysql2";

const getAll = async (): Promise<Message[]> => {
    Logger.info('Getting all messages from the database');
    const conn = await getPool().getConnection();
    const query = 'select * from lab2_messages';
    const [ rows ] = await conn.query(query);
    await conn.release();
    return rows;
}

const getOne = async (id: number): Promise<Message[]> => {
    Logger.info(`Getting message ${id} from the database`);
    const conn = await getPool().getConnection();
    const query = 'select * from lab2_messages where message_id = ?';
    const [ rows ] = await conn.query(query, [ id ]);
    await conn.release();
    Logger.info(rows);
    return rows;
}

const insert = async (message: string, convoId: number, userId: number): Promise<ResultSetHeader> => {
    Logger.info(`Adding message ${message} to the database`);
    const conn = await getPool().getConnection();
    const query = 'insert into lab2_messages (message, convo_id, user_id) values ( ?, ?, ?)';
    const [ result ] = await conn.query(query, [message, convoId, userId]);
    await conn.release();
    return result;
}

export { getAll, getOne, insert }