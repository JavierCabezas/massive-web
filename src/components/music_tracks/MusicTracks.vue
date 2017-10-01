<template>
    <div class="container">
        <div class="breadcrumb-wrapper">
            <div class="container">
                <h1>Music Tracks</h1>
            </div>
        </div>
        <bread-crumbs></bread-crumbs>
        <div class="space-60"></div>
        <div class="row">
            <div class="col-md-12">
                <ul class="product-filter-block list-inline clearfix">
                    <li> Title </li>
                    <li class="active"><a href="#">Top rated</a></li>
                    <li><a href="#">Otra categoría</a></li>
                    <li><a href="#">Una última</a></li>
                </ul>

                <music-track-list :items="items"></music-track-list>
            </div>
        </div>
    </div>
</template>

<script>
    import MusicTrackList from './MusicTrackList.vue'
    import BreadCrumbs from '../main/Breadcrumbs.vue'

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
            musicTrackList: MusicTrackList,
            breadCrumbs: BreadCrumbs
        }
    }
</script>