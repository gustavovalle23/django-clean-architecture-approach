const { SchemaRegistry, SchemaType } = require('@kafkajs/confluent-schema-registry')
const { readFileSync } = require('fs')
const { join } = require('path');


const registry = () => {
	return new SchemaRegistry({ host: 'http://schema-registry:8081/' })
}

async function encodePayload(payload) {
	const schemaRegistry = registry()
	const schema = readFileSync(join(__dirname, './book.proto')).toString();

	const { id } = await schemaRegistry.register({
		schema: schema,
		type: SchemaType.PROTOBUF
	}, { subject: 'Proto:Book' });

	const encodedValue = await schemaRegistry.encode(id, payload)
	return encodedValue
}

async function decodePayload(bufferedPayload) {
	const schemaRegistry = registry()
	const decodedValue = await schemaRegistry.decode(bufferedPayload)
	return decodedValue
}


module.exports = {
	encodePayload,
	decodePayload
}
