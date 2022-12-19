import { SchemaRegistry, SchemaType } from '@kafkajs/confluent-schema-registry';
import { readFileSync } from 'fs';
import { join } from 'path';


const registry = () => {
	return new SchemaRegistry({ host: 'http://schema-registry:8081/' })
}

const encodePayload = async (payload) => {
	const schemaRegistry = registry()
	const schema = readFileSync(join(__dirname, './book.proto')).toString();

	const { id } = await schemaRegistry.register({
		schema,
		type: SchemaType.PROTOBUF
	}, { subject: 'Proto:Book' });

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
