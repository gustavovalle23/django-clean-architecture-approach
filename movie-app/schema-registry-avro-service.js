import { SchemaRegistry, SchemaType } from '@kafkajs/confluent-schema-registry'


const schema = JSON.stringify({
	name: 'book',
	namespace: 'test',
	type: 'record',
	fields: [
		{ name: 'name', type: 'string' },
		{ name: 'days', type: 'string' }
	]
})

const registry = () => {
	return new SchemaRegistry({ host: 'http://schema-registry:8081/' })
}

const encodePayload = async (payload) => {
	const schemaRegistry = registry()

	const { id } = await schemaRegistry.register({
		schema,
		type: SchemaType.AVRO
	});

	const encodedValue = await schemaRegistry.encode(id, payload)
	return encodedValue
}

const decodePayload = async (bufferedPayload) => {
	const schemaRegistry = registry()
	const decodedValue = await schemaRegistry.decode(bufferedPayload)
	return decodedValue
}

export default {
	encodePayload,
	decodePayload
}
