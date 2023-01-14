import { Controller, Get, Inject } from '@nestjs/common';
import {
  ClientKafka,
  Ctx,
  EventPattern,
  KafkaContext,
  Payload,
  RmqContext,
} from '@nestjs/microservices';
import { Batch } from 'kafkajs';
import { debug } from 'console';
import { Book, BookSchemaRegistry } from './book';
import { AppService } from './app.service';

@Controller()
export class AppController {
  constructor(
    private readonly appService: AppService,
    @Inject('BOOK_SERVICE')
    private readonly client: ClientKafka,
  ) {}

  @Get()
  async getSchemaRegistry(): Promise<any> {
    const book = new Book('Book1', '21');
    const encodedMessage = await this.appService.encodePayload(book);
    const decodedMessage = await this.appService.decodePayload(encodedMessage);
    return this.client.emit('finish.book', { foo: 'bar' });
    return new BookSchemaRegistry(encodedMessage, decodedMessage);
  }

  @EventPattern('finish.book')
  finishBook(@Payload() { messages }: Batch, @Ctx() context: KafkaContext) {
    // debug(`Messages: ${messages}`);
    // debug(`Messages: ${context.getMessage()}`);
    // console.log(`Messages: ${messages}`);
    console.log(`Messages: ${JSON.stringify(context.getMessage())}`);
    // debug(`Finish the book ${name} in ${days} days`);
  }
}
