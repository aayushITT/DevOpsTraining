const { add, subtract } = require('./math');

test('adds 2 + 3 to equal 5', () => {
    expect(add(2, 3)).toBe(5);
});

test('subtracts 10 - 4 to equal 6', () => {
    expect(subtract(10, 4)).toBe(6);
});