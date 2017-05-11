<template>
    <div class="search-bar">
        <div class="container">
            <div class="row">
                <div class="col-sm-10 col-sm-offset-1">
                    <form>
                        <input type="text" class="form-control" placeholder="E.g. Blue T-shirt...">
                        <a href="#" @click.prevent="closeSearch()" class="search-close"><i class="fa fa-times"></i></a>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        methods:{
            closeSearch() {
                $('.search-close').click(function () {
                    $('.search-bar').slideUp('slow');
                });
            }
        }
    }
</script>