<template>
    <section class="featured-products">
        <div class="container">
            <h2 class="section-heading"> Popular Items</h2>
            <div class="row">
                <ul class="popularslider">
                    <li class="slide item_holder"><img src="../../img/women/1.jpg"/></li>
                    <li class="slide item_holder"><img src="../../img/men/1.jpg"/></li>
                    <li class="slide item_holder"><img src="../../img/women/2.jpg"/></li>
                    <li class="slide item_holder"><img src="../../img/men/2.jpg"/></li>
                    <li class="slide item_holder"><img src="../../img/women/1.jpg"/></li>
                    <li class="slide item_holder"><img src="../../img/men/1.jpg"/></li>
                    <li class="slide item_holder"><img src="../../img/women/2.jpg"/></li>
                    <li class="slide item_holder"><img src="../../img/men/2.jpg"/></li>
                    <li class="slide item_holder"><img src="../../img/women/1.jpg"/></li>
                </ul>
            </div>
        </div>
    </section>
</template>

<script>
    $(document).ready(function(){
        $(".popularslider").bxSlider({
            slideWidth: 200,
            minSlides: 3,
            maxSlides: 6,
            slideMargin: 10,
            auto: true
        });
    });
</script>