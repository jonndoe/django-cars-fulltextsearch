describe('Cars', function () {
  it('Displays the home page.', function () {
    cy.visit('/');
    cy.get('h1').should('contain', 'Cars');
  });
});

it('Displays a list of results.', function () {
  cy.intercept('GET', '**/api/v1/catalog/cars/**', { fixture: 'cars.json' }).as('getCars');

  cy.visit('/');
  cy.get('input#query').type('cabernet');
  cy.get('button').contains('Search').click();
  cy.wait('@getCars');
  cy.get('div.card-title').should('contain', 'Cabernet Sauvignon');
});