<template>
  <div class='movie-details'>
      <div class="detail-header">
        <button @click="$emit('back')" class="btn btn-back"><i class="far fa-arrow-alt-circle-left"></i>  Back</button>
        <button v-if="movie.is_fav" @click="$emit('fav_rem')" class="btn not-favorite"> 
          <!-- <i class="fas fa-star"></i> -->
         <!-- <i class="fas fa-star"></i> -->

         <i class="fas fa-star"></i> Remove from watch
           </button>
        <button v-else @click="$emit('fav_add')" class="btn  favorite "> <i class="fas fa-star"></i> Add to watch</button>


      </div>  
     <hr>
     <div class="details-content scrollbar2">

       <div class="details-images">
          <img
              class="background"
              :src="movie.cover"
              alt="Card image cap"
            >
       </div>
        <div class="details-info " >
          <h2> <span class="rating">{{movie.rating}} </span>  {{movie.title}}</h2>
          <h2 class="color-text2">{{movie.year}}</h2>
          <div class="line">
            <a :href="movie.imdb_url" class="imdb-link" target="_blank">     
              <img height="52" src="img/imdb.png" alt=""> 
            </a> 
              
            <a v-if="movie.youtubeId!=''" 
            :href="youtube_url" class="youtube-link" target="_blank">        <img height="52" src="img/youtube.png" alt=""> </a>

          </div>
          <div class="line" ><strong>Length: </strong> {{movie.length}} min</div>
          <div class="line" style="margin-bottom: 1rem"><strong>Genres: </strong> {{movie.genres}}</div>

          
          <div class="line"><strong>Director: </strong> {{movie.director}}</div>
          <div  class="line"><strong>Producer: </strong> {{movie.producer}}</div>

          <h4 class="line">Summary:</h4>
          <div  style="margin-bottom: 2rem">
            
          {{movie.plot}}

          </div>
       </div>
    
<!-- Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quos fugit cum explicabo impedit voluptatibus illo itaque dicta esse. Quae mollitia nihil rem possimus enim repellendus incidunt quia expedita tenetur explicabo. -->
     </div>
  </div>
</template>

<script>

export default {
  props: ['movie'],
  computed: {
    youtube_url() {
      return "https://www.youtube.com/embed/" + this.movie.youtubeId + "?autoplay=1";
    }
  }

}
</script>
<style lang="scss">
@import "../css/main.scss";
$row-height: 300px;
$header-height: 450px;

$color-silver: #dfe4ea;
$color-gray: #57606f;
$color-gray-2: #2f3542;
$color-black: #57606f;
$scale: 0.96;
$card-height: 180px;



.movie-details {
    position: absolute; top: 0; left: 0;
    width: 100%; height: 100%;
    background: white;
    color: #1F2041;
    padding: 1rem;
    z-index: 200;
    overflow: hidden;

    display: grid;
    grid-template-columns: 1fr;
    grid-template-rows: auto auto 1fr;
    max-height: 100%;

  background-image: url("~/img/movies.jpg");
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;    


.favorite {
          box-shadow: 0px 0px 2px $color-gray;
        background-color: $color-gray;
        color: white;
}

.not-favorite {
            // box-shadow: 0px 0px 2px $color-red;
        // background-color: $color-red;
        color: black;
        box-shadow: 0px 0px 2px $color-star;
        background-color: $color-star;
        // color: white;
        color: $color-gray;

      &:hover {
        color: $color-gray;
      }


}

    hr {
      margin-top: 10px;
      color: #1F2041;
    }
    .detail-header {
      display: flex;
      flex-wrap: wrap;
      align-items: baseline;
      // position: relative;

      h2 {
        margin-left: 10px;
        line-height: 2.2rem;
        
      color: #1F2041;
        // display: inline;
        // vertical-align: middle;
        // text-align: right;
        // position:absolute;top: 50%; left: 50%;
      }
    }

    .details-content {
      display: flex;
      flex-wrap: nowrap;
      // height: 100%;
      background: rgba(white,0.9);
      padding: 1rem;
      border: 1px solid $color-gray;
      border-radius: 5px;
      width: 100%;

      color: $color-text;
      text-align: left;
      margin-top: 0.5rem;
             overflow: auto;

            overflow: auto;
      
    // align-content: stretch;
    // align-items: flex-start;
    // align-content: flex-start;


        @media screen and (max-width: 500px) {
          & {
            //  height: 100%;
             flex-wrap: wrap;

          }

          div.details-info {
            // height: 100%;
            // overflow: hidden !important;
          }

          >div.details-images { 
            float: none;
            margin-right:0;
            width:auto;
            border:0;
            // width: 100%;
            text-align: center;
            vertical-align: middle;
            margin-left: auto;
            margin-right: auto;

            // border: 1px solid red;
           
            // border-bottom:2px solid #000;    
          }
        }


      > div.details-info {
        // display: inline;
        // flex: 50%;
        height: 100%;
        padding: 1rem;
        max-width: 500px;
        padding-bottom: 1rem;
        
        // * {
        //   height: 100%;
        // }
            // overflow: auto;
        // float: left;
      }

      .line {
        margin-bottom: 0.5rem;
      }

      > div.details-images {
       float: left;
      //  width: 50%;
       margin: 0.5rem;

       img {
         border: 1px solid $color-gray;
       }
      //  border: 1px solid red;
      }
    }

    @mixin hov {

      &:hover * {
        transform: scale(1.2);
      }
      &:active  * {
        transform: scale(0.9);
      }
    }


    .imdb-link {
      @include hov();
      font-size: 2.5rem;
      margin-right: 0.5rem;
      color: rgb(245, 197, 24); // from imdb page
      vertical-align: top;
      z-index: 102;
      position: relative;

      img {
        z-index: 100 !important;
        // position: absolute;
      }


    
    }

    
 

    .youtube-link {
      @include hov();

      font-size: 2.5rem;
      margin-right: 0.5rem;
      color: red; // from imdb page
    }

    img.background {
      // width: 50%;
      margin-top: 12px;
      max-width: 250px;
      max-height: 580px;
       margin-left: auto;
            margin-right: auto;


      background-size: cover;
      object-fit: cover;
      object-position: 0 0;
      border: 1px solid $color-silver;
    }
}
</style>


