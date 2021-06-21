describe('Cars', function () {
  it('Displays the home page.', function () {
    cy.visit('/');
    cy.get('h1').should('contain', 'Cars');
  });
});

it('Displays a list of results.', function () {
  cy.intercept('GET', '**/api/v1/catalog/cars/**', { fixture: 'cars.json' }).as('getCars');

  cy.visit('/');
  cy.get('input#country').type('US');
  cy.get('input#points').type('92');

  cy.get('input[placeholder="Enter a search term (e.g. cabernet)"]').type('cabernet');
  cy.get('button').contains('Search').click();
  cy.wait('@getCars');
  cy.get('div.card-title').should('contain', 'Cabernet Sauvignon');
});

it('Displays car search words.', function () {
  // Stub server
  cy.intercept(
    'GET', '**/api/v1/catalog/car-search-words/**',
    { fixture: 'car_search_words.json' }
  ).as('getCarSearchWords');

  cy.visit('/');
  cy.get('input[placeholder="Enter a search term (e.g. cabernet)"]')
    .type('cabarnet');
  cy.wait('@getCarSearchWords');
  cy.get('div#query').should('contain', 'cabernet');
});
