import { Controller, Get } from '@nestjs/common';
import { EventPattern, Payload } from '@nestjs/microservices';
import { debug } from 'console';
import { AppService } from './app.service';
import {
  SchemaRegistry,
  SchemaType,
  COMPATIBILITY,
} from '@kafkajs/confluent-schema-registry';
import { join } from 'path';
import { readFileSync } from 'fs';

class FinishBookMessage {
  name: string;
  days: number;
}

@Controller()
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Get()
  async getHello(): Promise<string> {
    const message = this.appService.getHello();

    const schemaRegistry = new SchemaRegistry(
      { host: 'http://localhost:8081' },
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

    const encodedMessage = schemaRegistry.encode(schemaRegistryId, { message });
    debug('Encoded message: ', encodedMessage);
    return message;
  }

  @EventPattern('finish.book')
  finishBook(@Payload() { name, days }: FinishBookMessage): any {
    debug(`Finish the book ${name} in ${days} days`);
  }
}
