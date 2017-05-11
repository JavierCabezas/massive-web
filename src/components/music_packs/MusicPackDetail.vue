<template>
    <div ng-controller="musicdetailController">
        <div class="space-60"></div>
        <div class="container">
            <div  class="row single-product">
                <div class="col-md-9">
                    <div class="row">
                        <div class="col-md-5 margin-b-30">
                            <div id="product-single" class="single-product-slider">
                                <div class="item">
                                    <a href="../../img/men/s-1.jpg" data-lightbox="roadtrip"> <img src="../../img/men/s-1.jpg" alt="Product image" class="img-responsive"></a>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-7">
                            <div class="product-detail-desc">
                                <h3 class="title"><a href="#">Origin of Symmetry</a></h3>
                                <h4>Autor</h4>
                                <span class="price">$200</span>
                                <span class="rating">
                                <a href="#">2 reviews</a>
                            </span>
                                <div class="add-buttons">
                                    <a href="#" data-toggle="tooltip" data-placement="top" title="Add to cart"
                                       class="btn btn-skin btn-lg"><i class="fa fa-shopping-cart"></i> Add to Cart</a>
                                </div>
                                <div id="cwrap">
                                    <div id="nowPlay">
                                        <h3 id="npAction">Playlist</h3>
                                        <div id="npTitle"></div>
                                    </div>
                                    <div id="audiowrap">
                                        <div id="audio0">
                                            <audio id="audio1" controls="controls" width="300">
                                                Your browser does not support the HTML5 Audio Tag.
                                            </audio>
                                        </div>
                                        <div id="extraControls">
                                            <button id="btnPrev" class="ctrlbtn">|&lt;&lt; Prev Track</button> <button id="btnNext" class="ctrlbtn">Next Track &gt;&gt;|</button>
                                        </div>
                                    </div>
                                    <div id="plwrap">
                                        <ul id="plUL">
                                            <li>
                                                <div class="plItem">
                                                    <div class="plTitle"><a href="#">Happy Birthday Variation: In the style of Beethoven</a></div>
                                                    <div class="plLength">0:55</div>
                                                </div>
                                            </li>
                                            <li>
                                                <div class="plItem">
                                                    <div class="plTitle"><a href="#">Wedding March Variation 1</a></div>
                                                    <div class="plLength">0:37</div>
                                                </div>
                                            </li>
                                            <li>
                                                <div class="plItem">
                                                    <div class="plTitle"><a href="#">Happy Birthday Variation: In the style of Tango</a></div>
                                                    <div class="plLength">1:05</div>
                                                </div>
                                            </li>
                                            <li>
                                                <div class="plItem">
                                                    <div class="plTitle"><a href="#">Wedding March Variation 2</a></div>
                                                    <div class="plLength">0:40</div>
                                                </div>
                                            </li>
                                            <li>
                                                <div class="plItem">
                                                    <div class="plTitle"><a href="#">Random Classical</a></div>
                                                    <div class="plLength">0:59</div>
                                                </div>
                                            </li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div><!--single product details end-->
                    <div class="row">
                        <div class="col-md-12 item-more-info">
                            <div ng-controller="detailController" id="detail">
                                <!-- Tab panes -->
                                <div class="col-sm-12">
                                    <h2>Description</h2>
                                    <p>Origin of Symmetry —en español: El Origen de la Simetría es el segundo álbum de
                                        estudio de la banda británica de rock alternativo, Muse, lanzando en el verano de
                                        2001 por Mushroom Records en el Reino Unido. Sus sencillos fueron “Plug in Baby”,
                                        “New Born”, “Bliss” e “Hyper Music/Feeling Good”. Maverick, que lanzó Showbiz en
                                        Estados Unidos, pidió que los falsos vocales fueran eliminados, pues creían que
                                        obstaculizaba su posibilidad de ser puesta en radio. Muse se negó a este cambio
                                        por comprometer su integridad artística (o arruinar la canción). Por esta razón,
                                        el disco no fue lanzado en los Estados Unidos hasta 2005.</p>
                                    <div class="space-40"></div>
                                </div>

                            </div>
                        </div>
                    </div>

                </div>

                <div class="col-md-3">
                    <div class="sidebar-widget">
                        <h3>Categories</h3>
                        <ul class="list-unstyled">
                            <li><a href="#">Category 1</a></li>
                            <li><a href="#">Category 2</a></li>
                            <li><a href="#">Category 3</a></li>
                            <li><a href="#">Category 4</a></li>
                            <li><a href="#">Category 5</a></li>
                        </ul>
                    </div><!--sidebar-widget end-->
                </div><!--sidebar col-->
            </div>
            <div class="space-60"></div>
            <div class="similar-products">
                <div class="row">
                    <section class="similar-prods">
                        <div class="container">
                            <h2 class="section-heading" translate="similarprod">Similar Packs</h2>
                            <div class="row">
                                <ul class="similarlider">
                                    <li class="item_holder"><img src="../../img/women/1.jpg"/></li>
                                    <li class="slide item_holder"><img src="../../img/men/1.jpg"/></li>
                                    <li class="slide item_holder"><img src="../../img/women/1.jpg"/></li>
                                    <li class="slide item_holder"><img src="../../img/men/1.jpg"/></li>
                                    <li class="slide item_holder"><img src="../../img/women/1.jpg"/></li>
                                    <li class="slide item_holder"><img src="../../img/men/1.jpg"/></li>
                                    <li class="slide item_holder"><img src="../../img/women/1.jpg"/></li>
                                    <li class="slide item_holder"><img src="../../img/men/1.jpg"/></li>
                                    <li class="slide item_holder"><img src="../../img/women/1.jpg"/></li>
                                </ul>
                            </div>
                        </div>
                    </section>
                </div>
                <!--owl end-->
            </div><!--similar products-->
        </div>
    </div>
</template>