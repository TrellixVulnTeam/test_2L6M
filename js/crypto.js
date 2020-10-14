const crypto = require('crypto')

const KEY = 'RwcmlVpgRwcmlVpg'
const IV = '4e5Wa71fYoT7MFEX'

function encrypt(str) {
    const cipher = crypto.createCipheriv('aes-128-cbc', KEY, IV)
    const encrypted = cipher.update(str);
    return Buffer.concat([encrypted, cipher.final()]).toString('base64')
}

function decrypt(encrypted) {
    const buf = Buffer.from(encrypted, 'base64')
    const cipher = crypto.createDecipheriv('aes-128-cbc', KEY, IV)
    const decrypted = cipher.update(buf);
    return Buffer.concat([decrypted, cipher.final()]).toString('utf-8')
}

const encrypted = encrypt('かかかかかっかかあｋ')
console.log(encrypted)
console.log(decrypt(encrypted))
