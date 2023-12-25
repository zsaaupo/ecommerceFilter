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
});


// $('#filer').click(function(){
//     $('.row').html(``)
//     // var data_search = $('#name').val()
//     var url = "/products/"
//     $.ajax({
//     type:"GET",
//     url: url,
//     success: function(value){
//         for(let i = 0; i < value.length; i++){
//             $('.card').append(`
//             <div class="col-lg-4">
//                 <img class="thumbnail" src="${ value[i].imageURL }" />
//                 <div class="box-element product">
//                 <h6><strong>${ value[i].name }</strong></h6>
//                 <hr />
//                 <button data-product="" data-action="add" class="btn btn-outline-secondary add-btn update-cart">Add to Cart</button>
//                 <h4 style="display: inline-block; float: right"><strong>${ value[i].price }</strong></h4>
//                 </div>
//             </div>
//             `)
//         }
//     },
//     error: function(errormsg){
//         console.log(errormsg)
//     }
// });
// })