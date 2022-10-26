export default () => ({
  kafka: {
    brokers: JSON.parse(`["kafka:9092"]`),
    clientId: 'book-app',
    groupId: 'book-app-consumer',
  },
});
