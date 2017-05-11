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

                <music-pack-list :items="items"></music-pack-list>

                <nav>
                    <ul class="pagination pull-right clearfix">
                        <li>
                            <a href="#" aria-label="Previous">
                                <span aria-hidden="true">&laquo;</span>
                            </a>
                        </li>
                        <li class="active"><a href="#">1</a></li>
                        <li><a href="#">2</a></li>
                        <li><a href="#">3</a></li>
                        <li><a href="#">4</a></li>
                        <li><a href="#">5</a></li>
                        <li>
                            <a href="#" aria-label="Next">
                                <span aria-hidden="true">&raquo;</span>
                            </a>
                        </li>
                    </ul>
                </nav>
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
    import MusicpackList from './MusicPackList.vue'

    export default {
        data () {
            return {
                items: [
                    {
                        id: 1,
                        link: "#",
                        img: '../src/img/bg/bg-1.jpg',
                        title: 'Title 2',
                        text: 'INGLÉS Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum commodo tellus nisl, ac fermentum ligula laoreet eu. In consequat diam sed est tempus convallis.',
                        price: 24033
                    },
                    {
                        id: 2,
                        link: "#",
                        img: '../src/img/bg/bg-1.jpg',
                        title: 'Title 2',
                        text: 'INGLÉS Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum commodo tellus nisl, ac fermentum ligula laoreet eu. In consequat diam sed est tempus convallis.',
                        price: 24033
                    },
                    {
                        id: 3,
                        link: "#",
                        img: '../src/img/bg/bg-1.jpg',
                        title: 'Title 2',
                        text: 'INGLÉS Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum commodo tellus nisl, ac fermentum ligula laoreet eu. In consequat diam sed est tempus convallis.',
                        price: 24033
                    }
                ]
            }
        },
        components: {
            musicPackList: MusicpackList
        }
    }
</script>