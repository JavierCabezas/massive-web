<template>
    <div class="container">
        <!--breadcrumb start-->
        <div class="breadcrumb-wrapper">
            <div class="container">
                <h1>Blog</h1>
            </div>
        </div>
        <!--end breadcrumb-->

        <div class="space-60"></div>
        <div class="container">
            <div v-for="i in [1, 2, 3]" class="col-sm-4">
                <div class="blog-item">
                    <a href="#">
                        <img src="../../img/bg/bg-1.jpg" class="img-responsive" alt="">
                    </a>
                    <div class="blog-desc">
                        <ul>
                            <li><a href="#" class="tag"><i class="fa fa-tag"></i> Lorem</a></li>
                        </ul>
                        <h4 class="title"><a href="#"> Title </a></h4>
                        <p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum commodo tellus nisl, ac fermentum ligula laoreet eu. In consequat diam sed est tempus convallis.</p>
                        <a href="#" class="btn btn-skin">Continue</a>
                    </div><!--blog desc-->
                </div><!--blog item-->
            </div><!--grid blog-->
            <nav>
                <ul class="pagination pull-right clearfix">
                    <li>
                        <a href="#" aria-label="Previous">
                            <span aria-hidden="true">«</span>
                        </a>
                    </li>
                    <li class="active"><a href="#">1</a></li>
                    <li><a href="#">2</a></li>
                    <li><a href="#">3</a></li>
                    <li><a href="#">4</a></li>
                    <li><a href="#">5</a></li>
                    <li>
                        <a href="#" aria-label="Next">
                            <span aria-hidden="true">»</span>
                        </a>
                    </li>
                </ul>
            </nav>
        </div>
    </div>
</template>