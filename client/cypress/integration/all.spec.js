describe('Cars', function () {
  it('Displays the home page.', function () {
    cy.visit('/');
    cy.get('h1').should('contain', 'Cars');
  });
});