import {
  COMPATIBILITY,
  SchemaRegistry,
  SchemaType,
} from '@kafkajs/confluent-schema-registry';
import { Injectable } from '@nestjs/common';
import { readFileSync } from 'fs';
import { join } from 'path';

@Injectable()
export class AppService {
  getHello(): string {
    return 'Hello World!';
  }

  async encodeMessage(message: string): Promise<Buffer> {
    const schemaRegistry = new SchemaRegistry(
      { host: 'http://schema-registry:8081' },
      {
        [SchemaType.PROTOBUF]: {
          messageName: 'Book',
        },
      },
    );
    const schema = readFileSync(join(__dirname, '../book.proto')).toString();
    const { id: schemaRegistryId } = await schemaRegistry.register(
      {
        type: SchemaType.PROTOBUF,
        schema,
      },
      {
        compatibility: COMPATIBILITY.BACKWARD,
        subject: 'book.app.Book',
      },
    );

    const encodedMessage = await schemaRegistry.encode(schemaRegistryId, {
      message,
    });
    return encodedMessage;
  }
}
