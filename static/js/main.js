$(document).ready(function () {
  $.ajax({
    type: "GET",
    url: "/products/",
    success: function (data) {
      renderProducts(data);
    },
    error: function (error) {
      console.log("Error fetching products:", error);
    }
  });
});

$('#filer').click(function (event) {
  event.preventDefault();

  var selectedValues = {
    "category": [],
    "brand": [],
    "seller": [],
    "warranty": [],
    "productType": []
  };

  $('input[name="options"]:checked').each(function () {
    var category = $(this).attr('id');
    selectedValues[category].push(parseInt($(this).val()));
  });
  console.log('Selected Values:', selectedValues);

  $.ajax({
    type: "POST",
    url: "/products/filter/",
    contentType: "application/json; charset=utf-8",
    dataType: "json",
    data: JSON.stringify(selectedValues),
    success: function (data) {
      console.log(data);
      renderProducts(data);
    },
    error: function (error) {
      console.log(error);
    }
  });
})

function renderProducts(products) {
  $('.row').html('');

  for (let i = 0; i < products.length; i++) {
    $('.row').append(`
        <div class="col-lg-4">
          <img class="thumbnail" src="${products[i].image}" style='width:300px; height:300px;' />
          <div class="box-element product">
            <h6><strong>${products[i].name}</strong></h6>
            <hr />
            <button data-product="" data-action="add" class="btn btn-outline-secondary add-btn update-cart">Add to Cart</button>
            <h4 style="display: inline-block; float: right"><strong>${products[i].price}</strong></h4>
          </div>
        </div>
      `);
  }
}