<template>
    <div class="container">
        <div class="row">
            <div class="col-md-8">
                <ul class="product-filter-block list-inline clearfix">
                    <li> Title </li>
                    <li class="active"><a href="#">Top rated</a></li>
                    <li><a href="#">Otra categoría</a></li>
                    <li><a href="#"> UNa última</a></li>
                </ul>

            </div>

            <div class="col-md-3 col-md-offset-1">
                <div class="sidebar-widget">
                    <h3 translate="categories"></h3>
                    <ul class="list-unstyled">
                        <li><a href="#">New Arrivals</a></li>
                        <li><a href="#">Men</a></li>
                        <li><a href="#">Women</a></li>
                        <li><a href="#">T-shirts</a></li>
                        <li><a href="#">Shoes</a></li>
                        <li><a href="#">Handbags</a></li>
                        <li><a href="#">Accessories</a></li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

    export default {
        data () {
            return {
                items: [ ]
            }
        },
        created: function () {
            let vm = this;
            let url = vm.url_backend + '/site/music-tracks';

            $.ajax({
                url: url,
                success: function (result) {
                    vm.items = result;
                }
            });
        },
        components: {
           
        }
    }
</script>