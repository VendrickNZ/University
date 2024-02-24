const data = require('./users.json');
const users = data.users;
const bodyParser = require('body-parser');
const express = require('express');
const app = express();

app.use(bodyParser.json());
console.log(users);

app.get('/users', (req, res) => {
    res.status(200).send(users);
});

app.get('/users/:id', (req, res) => {
    const id = req.params.id
    let response = `No user with id ${id}`;
    for (const user of users) {
        if (parseInt(id, 10) === user.id) {
            response = user;
            break;
        }
    }
    res.status(200).send(response);
});

app.post('/users', (req, res) => {
    const newUser = req.body;
    users.push(newUser);
    res.status(201)
        .send(users);
})

app.put('/users/:id', (req, res) => {
    const id = req.params.id;
    const updatedUser = req.body;
    for (const user of users) {
        if (parseInt(id, 10) === user.id) {
            const index = users.indexOf(user);
            users[index] = updatedUser;
            break;
        }
        res.status(200)
            .send(updatedUser);
    }
})

app.delete('/users/:id', (req, res) => {
    const id = req.params.id;
    for (const user of users) {
        if (parseInt(id, 10) === user.id) {
            const index = users.indexOf(user);
            users.splice(index, 1);
        }
    }
    res.send(users);
});

app.put('/users/:id/follow', (req, res) => {
    const userId = parseInt(req.params.id, 10);
    const targetUserId = parseInt(req.body.targetUserId, 10);

    const user = users.find(user => user.id === userId);
    const targetUser = users.find(user => user.id === targetUserId);

    if (!user || !targetUser) {
        return res.status(404).send('User not found');
    }

    if (!user.following.includes(targetUserId)) {
        user.following.push(targetUserId);
    }

    res.status(200).send(user);
});

app.delete('/users/:id/unfollow', (req, res) => {
    const userId = parseInt(req.params.id, 10);
    const targetUserId = parseInt(req.body.targetUserId, 10);

    const user = users.find(user => user.id === userId);
    const targetUser = users.find(user => user.id === targetUserId);

    if (!user || !targetUser) {
        return res.status(404).send('User not found');
    }

    const index = user.following.indexOf(targetUserId);
    if (index !== -1) {
        user.following.splice(index, 1);
    }

    res.status(200).send(user);
});


app.get('/users/:id/following', (req, res) => {
    const userId = parseInt(req.params.id, 10);
    const user = users.find(user => user.id === userId);

    res.status(200).send(user.following)
})

app.listen(3000, () => {
    console.log("Listening on port 3000");
})

