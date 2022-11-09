export class Book {
  name: string;
  days: string;

  constructor(name: string, days: string) {
    this.name = name;
    this.days = days;
  }
}

export class BookSchemaRegistry {
  encoded: Buffer;
  decoded: Book;

  constructor(encoded: Buffer, decoded: Book) {
    this.encoded = encoded;
    this.decoded = decoded;
  }
}
