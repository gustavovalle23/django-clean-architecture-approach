const { Kafka } = require('kafkajs')
const { SchemaRegistry, SchemaType, COMPATIBILITY } = require('@kafkajs/confluent-schema-registry')
const { readFileSync } = require('fs')
const { join } = require('path');
const { debug } = require('console');

async function register(schema, registry) {
	const { id } = await registry.register(
		{
			type: SchemaType.PROTOBUF,
			schema,
		},
		{
			compatibility: COMPATIBILITY.BACKWARD,
			subject: 'book.app.Book',
		},
	);
	return { id }
}

class Book {
	constructor(name, days) {
		this.name = name
		this.days = days
	}
}


async function run() {
	const book = new Book('Book 1', 20)


	const kafka = new Kafka({ clientId: 'movie-app', brokers: ['kafka:9092'] })
	const schemaRegistry = new SchemaRegistry({ host: 'http://schema-registry:8081/' }, {
		[SchemaType.PROTOBUF]: {
			messageName: 'Book',
		},
	})
	const schema = readFileSync(join(__dirname, './book.proto')).toString();
	const { id: schemaRegistryId } = await register(schema, schemaRegistry)

	const encodedMessage = await schemaRegistry.encode(schemaRegistryId, {
		book,
	  });

	debug(encodedMessage)
	const decoded = await schemaRegistry.decode(encodedMessage)
	debug(decoded)
}

run()