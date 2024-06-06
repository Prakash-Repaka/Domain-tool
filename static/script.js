


function cleanData(data) {
    
    let domainName = data.domain_name.map(name => name.replace(/[\[\]']/g, ''));
    document.getElementById('domain-name').innerText = domainName.join(', ');

    
    document.getElementById('registrar').innerText = data.registrar.replace(/[\[\]']/g, '');

    
    let creationDate = data.creation_date.map(date => date.replace(/[\[\]']/g, ''));
    document.getElementById('creation-date').innerText = creationDate.join(', ');

    
    let expirationDate = data.expiration_date.map(date => date.replace(/[\[\]']/g, ''));
    document.getElementById('expiration-date').innerText = expirationDate.join(', ');
}




window.addEventListener('DOMContentLoaded', function() {
    
    cleanData(results);
});
