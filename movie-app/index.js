const express = require('express')

const { decodePayload, encodePayload } = require('./encode-message')

const app = express()
const port = 3000

app.get('/', async (req, res) => {
	const payload = { name: 'Book1', days: '20' }
	const encodedMessage = await encodePayload(payload)
	const decodedMessage = await decodePayload(encodedMessage)
	res.send({ originalMessage: payload, encodedMessage, decodedMessage})
})


app.listen(port, () => {
	console.log(`Listeing on port ${port}`)
})
