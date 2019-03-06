<style lang="scss">
@import url('../css/main.scss');

$color-silver: #dfe4ea;
$color-gray: #57606f;
$color-gray-2: #2f3542;
$color-black: #57606f;
$scale: 0.96;

  h2 {
    margin-bottom: 1rem;
  }

.cards {
  display: flex;
  flex-wrap: wrap;
  // justify-content: space-between;
  // border: 10px solid red;
  padding: 0px;
  margin: 0px;

  margin-top: 0.5rem;

  overflow: visible;

 flex-direction: row;
  justify-content: center;
  flex-wrap: wrap;

  
    align-content: flex-start;

  // &::after {
  //   content: '';
  //   flex: auto;
  //           // margin: 0;
  //   // margin-right: 0
  //   // margin-left: -50px;
  //   // width: 240px;
  // }



  a,
  a:link,
  a:hover,
  a:active,
  p:hover,
  a:-webkit-any-link,
  .noDecoration,
  a:link,
  a:visited {
    text-decoration: none;
    text-decoration: none !important;
    box-shadow: none;
  }
  > p {

    margin: 0;
    margin-right: 0;
    margin-left: 0;
    display: block;
  }

  .item {
        margin: 0;
    margin-right: 0;
    margin-left: 0;
  }

  .card {
    position: relative;
    margin-left: auto;
    margin-right: auto;
    border: 0;
    margin-left: 10px;
    margin-right: 10px;
    width: 180px;



    // margin-right: 15px;
    // height: 250px;
    // margin-right: 5px;
    border: 1px $color-silver;
    margin-bottom: 10px;

    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
    transition: 0.3s;
    cursor: pointer;
    background: white;
    color: black;

    &:hover {
      box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
      transform: translateY(-5px); // top: -10px;

       .favorite {
        opacity: 0.7 !important;
      }
    }
    &:active {
      transform: scaleX($scale) scaleY($scale);
    }

    .badges {
      position: absolute;
      margin-left: 5px;
      margin-top: 5px;
      display: flex;
    }

    .lang {
      position: absolute;
      right: 10px;
      top: 5px;
      opacity: 0.7;
    }

    img.background {
      width: 180px;
      height: 170px;
      background-size: cover;
      object-fit: cover;
      object-position: 0 0;
      border-bottom: 1px solid $color-silver;
    }

    .image-top {
      position: relative;

      .positive {
        display: block;
        opacity: 0;
        position: absolute;
        outline:none;
        font-family: "Avenir", Helvetica, Arial, sans-serif;
                border: none;
                     cursor: pointer;
                     color: white;
                     
         font-size: 18px;
        width: 50%;
        height: 170px;
        left: 50%;
        top: 0;
        background-color: rgba(green,0.5);
        z-index: 100;

        &:hover {
          opacity: 1;
        }
      }

      .negative {
        display: block;
                outline:none;
                border: none;
                     cursor: pointer;
                     
        font-family: "Avenir", Helvetica, Arial, sans-serif;
        opacity: 0;
        // visibility: hidden;
        position: absolute;
         color: white;
         font-size: 18px;
        width: 50%;
        height: 170px;
        left: 0;
        top: 0;
        background-color: rgba(red,0.5);
        z-index: 100;

                &:hover {
                  opacity: 1;

        }
      }

      .btn-round {
             display: inline-block;
          border-radius: 60px;
          box-shadow: 0px 0px 2px  #D8AB00;
          padding: 0.5em 0.6em;
          cursor: pointer;
          color: white;

          display: inline-block;
          border-radius: 60px;
          box-shadow: 0px 0px 2px  #D8AB00;
          padding: 0.5em 0.6em;
          cursor: pointer;
          background-color: #f1c40f;
          color: white;
          // margin-top: -70px;
          // margin-right: -30px;
          margin-left: auto;
          right: 5px;
          bottom: -10px;
          position: absolute;
          outline:none;
          z-index: 101;


      }

      .minus {
      box-shadow: 0px 0px 2px  #CE3323;
      background-color: #e74c3c;
        // opacity: 0;

      }


      .favorite {
   
          box-shadow: 0px 0px 2px  #D8AB00;
          // margin-top: -70px;
          // margin-right: -30px;
          right: 5px;
          bottom: -10px;
          position: absolute;


           
           
           }
     

    }

   

    .content {
      margin-top: 15px;
      padding: 0px 16px 5px 16px;
;
      .badge {
        margin-left: 5px;
      }

      &:hover {
        text-decoration: none !important;
      }
      // height: 120px;

      .title {
        margin: 0;
        display: flex;
        justify-content: space-between;

        h4 {
          display: inline;
          margin-right: auto;
          margin: 0;
          padding: 0;
        }

        .year {
          display: inline;

          color: #57606ffb;
          text-align: right;
          font-size: 0.8rem;
          font-weight: 600;
        }
      }

  

      p.text {
        text-align: justify;
        color: $color-black;
        text-decoration: none;
        font-size: 0.7rem;
        margin: 0;
        padding: 0;

        &:hover {
          text-decoration: none;
        }
      }
    }
  }
}
</style>

<template>
  <div class="item">
    <a :href="link" class="noDecoration">
      <div class="card">




        <!-- <div class="badges">
          <badge v-for="b in badges">{{b}}</badge>
        </div> -->
        <!-- <div class="lang">
          <img :src="lang=='pl' ? $withBase('/pl.png') :  $withBase('/en.png') " width="32px" :alt="lang">
        </div> -->

<div class="image-top">
       <img class="background" :src="img" alt="Card image cap">

        <button class="negative" v-if="islist">
          <i class="fas fa-thumbs-down"></i>
          <div>
             Not Like this
          </div>
        </button>
        <button class="positive" v-if="islist">
               <i class="fas fa-thumbs-up"></i>
                         <div>
              Like this 
          </div>
        </button>
        
        <button class="btn-round minus" v-if="!islist" @click.stop="$emit('fav_rem')">
          <i class="fas fa-minus"></i>
        </button>
<!-- 
            <button class="btn-round  negative-mob" v-if="islist" @click.stop="$emit('fav_add')">
          <i class="fas fa-thumbs-down"></i>
        </button>

         <button class="btn-round positive-mob" v-if="islist" @click.stop="$emit('fav_add')">
          <i class="fas fa-thumbs-up"></i>
        </button> -->

     

        <button class="btn-round  favorite" v-if="islist" @click.stop="$emit('fav_add')">
          <i class="fas fa-star"></i>
        </button>

</div>
 

        <div class="content">
          <div class="title">
            <h4>{{title}}</h4>
            <span class="year">{{year}}</span>
          </div>

          <!-- <p class="text">{{description}}</p> -->
        </div>
      </div>
    </a>

  </div>
</template>

<script>

function isMobileDevice() {
    return (typeof window.orientation !== "undefined") || (navigator.userAgent.indexOf('IEMobile') !== -1);
};

export default {
  props: ['title','islist',  'year', 'badge', 'description', 'lang', 'img', 'link'],
  computed: {
    badges() {
      if (this.badge == null || this.badge == '') return []
      return this.badge.split(',')
    },

    isMobile() {
      return (typeof window.orientation !== "undefined") || (navigator.userAgent.indexOf('IEMobile') !== -1);
    }
  }
}
</script>
