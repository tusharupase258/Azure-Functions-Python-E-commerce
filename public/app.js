async function loadProducts(){
  try{
    const res = await fetch('products.json');
    const products = await res.json();
    const grid = document.getElementById('grid');
    grid.innerHTML = products.map(p => `
      <div class="card">
        <h3>${p.name}</h3>
        <div class="price">$${p.price.toFixed(2)}</div>
      </div>`
    ).join('');
  }catch(e){
    document.getElementById('grid').innerHTML = '<div class="card">Failed to load products.json</div>';
  }
}
loadProducts();
