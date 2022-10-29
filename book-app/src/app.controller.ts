import { Controller, Get } from '@nestjs/common';
import { EventPattern, Payload } from '@nestjs/microservices';
import { debug } from 'console';
import { Book } from './book';
import { AppService } from './app.service';

class SchemaRegistryExample {
  encoded: Buffer;
  decoded: Book;

  constructor(encoded: Buffer, decoded: Book) {
    this.encoded = encoded;
    this.decoded = decoded;
  }
}

@Controller()
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Get()
  async getSchemaRegistry(): Promise<SchemaRegistryExample> {
    const book = new Book('Book1', '21');
    const encodedMessage = await this.appService.encodePayload(book);
    const decodedMessage = await this.appService.decodePayload(encodedMessage);
    return new SchemaRegistryExample(encodedMessage, decodedMessage);
  }

  @EventPattern('finish.book')
  finishBook(@Payload() { name, days }: Book): any {
    debug(`Finish the book ${name} in ${days} days`);
  }
}
