import {getPool} from '../../config/db';
import Logger from '../../config/logger';
import { ResultSetHeader} from "mysql2";

const getAll = async (): Promise<User[]> => {
    Logger.info('Getting all users from the database');
    const conn = await getPool().getConnection();
    const query = 'select * from lab2_users';
    const [ rows ] = await conn.query(query);
    await conn.release();
    return rows;
}

const getOne = async (id: number): Promise<User[]> => {
    Logger.info(`Getting user ${id} from the database`);
    const conn = await getPool().getConnection();
    const query = 'select * from lab2_users where user_id = ?';
    const [ rows ] = await conn.query(query, [ id ] );
    await conn.release();
    return rows;
}

const insert = async (username: string): Promise<ResultSetHeader> => {
    Logger.info(`Adding user ${username} to the database`);
    const conn = await getPool().getConnection();
    const query = 'insert into lab2_users (username) values ( ? )';
    const [ result ] = await conn.query(query, [username]);
    await conn.release();
    return result;
}

const alter = async (): Promise<any> => {
    return null;
}

const remove = async (): Promise<any> => {
    return null;
}

export {getAll, getOne, insert, alter, remove }