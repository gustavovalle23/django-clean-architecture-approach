import { SchemaRegistry, SchemaType } from '@kafkajs/confluent-schema-registry';
import { Injectable } from '@nestjs/common';
import { readFileSync } from 'fs';
import { join } from 'path';
import { Book } from './book';

@Injectable()
export class AppService {
  registry() {
    return new SchemaRegistry({ host: 'http://schema-registry:8081/' });
  }

  async encodePayload(payload: Book): Promise<Buffer> {
    const schemaRegistry = this.registry();
    const schema = readFileSync(join(__dirname, '../book.proto')).toString();

    const { id } = await schemaRegistry.register(
      {
        schema: schema,
        type: SchemaType.PROTOBUF,
      },
      { subject: 'Proto:Book' },
    );

    const encodedValue = await schemaRegistry.encode(id, payload);
    return encodedValue;
  }

  async decodePayload(bufferedPayload: Buffer): Promise<Book> {
    const schemaRegistry = this.registry();
    const decodedValue = await schemaRegistry.decode(bufferedPayload);
    return this.toObject(decodedValue);
  }

  toObject(payload: any) {
    return new Book(payload?.name, payload?.days);
  }
}
