const { SchemaRegistry, SchemaType } = require('@kafkajs/confluent-schema-registry')


const schema = {
	name: 'book',
	namespace: 'test',
	type: 'record',
	fields: [
		{ name: 'name', type: 'string' },
		{ name: 'days', type: 'string' }
	]
}

const registry = () => {
	return new SchemaRegistry({ host: 'http://schema-registry:8081/' })
}

async function encodePayload(payload) {
	const schemaRegistry = registry()

	const { id } = await schemaRegistry.register({
		schema: JSON.stringify(schema),
		type: SchemaType.AVRO
	});

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
