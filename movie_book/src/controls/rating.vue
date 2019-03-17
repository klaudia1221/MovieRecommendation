<template>
  <div class="star-rating animated  shake ">
    <label
      class="star-rating__star "
      v-for="rating in ratings"
      :key="rating"

      :class="{'is-selected': ((temp_value >= rating) && temp_value != null), 'is-disabled': disabled}"
      v-on:click="set(rating)"
      v-on:mouseover="star_over(rating)"
      v-on:mouseout="star_out"
    >
      <input
        class="star-rating star-rating__checkbox "
        type="radio"
        :value="rating"
        :name="name"
         @input="set($event.target.value)"
        :disabled="disabled"
      >★</label></div>
</template>
<script>

// https://codepen.io/olimorris/pen/yOYBjd
export default {
    props: {
    'name': String,
    'value': null,
    'id': String,
    'disabled': Boolean,
    'required': Boolean
  },
  /*
   * Initial state of the component's data.
   */
  data: function() {
    return {
      temp_value: null,
      ratings: [1, 2, 3, 4, 5]
    };
  },
  methods: {
    /*
     * Behaviour of the stars on mouseover.
     */
    star_over: function(index) {
      var self = this;



      if (!this.disabled) {
        // console.log(index);
        this.temp_value = index;
        // this.$emit('input', this.value);
        // return this.value = index;
      }
    },

    /*
     * Behaviour of the stars on mouseout.
     */
    star_out: function() {
      var self = this;

      if (!this.disabled) {
        this.temp_value = this.value;
        // return this.value = this.temp_value;
      }
    },

    /*
     * Set the rating.
     */
    set: function(value) {
      var self = this;
      if (!this.disabled) {
        this.temp_value = value;
        this.$emit('input',value);
      }
    }
  }
};

</script>

<style lang="scss">

%visually-hidden {
  position: absolute;
  overflow: hidden;
  clip: rect(0 0 0 0);
  height: 1px;
  width: 1px;
  margin: -1px;
  padding: 0;
  border: 0;
}

.star-rating {

  &:hover .is-selected {
        color: blue;
  }
  &__star {
    display: inline-block;
    padding: 3px;
    vertical-align: middle;
    line-height: 1;
    font-size: 1.5em;
    color: #ababab;
    transition: color 0.2s ease-out;

    &:hover {
      cursor: pointer;
    }

    &.is-selected {
      color: #ffd700;


    }

    &.is-disabled:hover {
      cursor: default;
    }
  }

  &__checkbox {
    @extend %visually-hidden;
  }
}
</style>
