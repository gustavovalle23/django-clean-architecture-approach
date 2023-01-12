import express from 'express'
import { encodePayload, decodePayload } from './src/infra/services/schema-registry-proto-service.js'


const app = express()
const port = 3000

app.get('/movie', async (req, res) => {
	const payload = { name: 'Book1', days: '20' }
	const encodedMessage = await encodePayload(payload)
	const decodedMessage = await decodePayload(encodedMessage)
	res.send({ originalMessage: payload, encodedMessage, decodedMessage })
})

app.post('/movie', async (req, res) => {
	const payload = { name: 'Book1', days: '20' }
	const encodedMessage = await encodePayload(payload)
	const decodedMessage = await decodePayload(encodedMessage)
	res.send({ originalMessage: payload, encodedMessage, decodedMessage })
})



app.listen(port, () => {
	console.log(`Listeing on port ${port}`)
})
