<template>
    <div class="container">
        <div class="row">
            <div class="col-md-12">
                <ul class="product-filter-block list-inline clearfix">
                    <li> Title </li>
                    <li class="active"><a href="#">Top rated</a></li>
                    <li><a href="#">Otra categoría</a></li>
                    <li><a href="#"> UNa última</a></li>
                </ul>


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