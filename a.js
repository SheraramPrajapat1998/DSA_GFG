// Q. 1
// var o = Object.assign(Object.create(null), { a: 1 }, { a: 2 }, { a: 3 });
// Object.assign(Object.prototype, { f: function() {} });

// for (var i in o) {
// console.log(o[i]);
// }
// Ans: [ 31.622776601683793, 96.23408959407264, 385.84582413186746 ]


// Q. 2
// function getAge(...args) {
//   console.log(typeof args);
//   }
  
//   getAge(21);
// Ans: object


// Q. 3
// 'use strict'
 
//  //regular function
//  let add = function (m,n) {
//  return m+n
//  }
//  //constructor function
//  let SuperHero = function (strength) {
//  if(!new.target) throw 'Vashi: Black sheep';
//  this.strength = strength;
//  }
 
//  let Flash = new SuperHero('Fast');
//  let ProfessorX = new SuperHero('Mind Control');
 
//  let Planet = function (_planet) {
//  this.setPlanet = function (planet) {
//  _planet = planet;
//  }
//  this.getPlanet = function () {
//  return _planet;
//  }
//  }
//  let ReachPlanet = new Planet("Venus");
//  console.log(ReachPlanet.getPlanet());
//  ReachPlanet.setPlanet("Mars");
//  console.log(ReachPlanet.getPlanet());

// Ans: Venus
//      Mars

// Q.4 
// class Chameleon {
//   static colorChange(newColor) {
//     this.newColor = newColor;
//     return this.newColor;
//   }
  
//   constructor({ newColor = 'green' } = {}) {
//     this.newColor = newColor;
//   }
// }
// const freddie = new Chameleon({ newColor: 'purple' });
// console.log(freddie.colorChange('orange'));
// Ans: TypeError: freddie.colorChange is not a function


// Q. 5
var foo = "foo";
 
(function (innerFoo) {
  console.log(innerFoo);
})(foo);

(function () {
  var foo = "bar";
  console.log(foo);
})();

let f1 = function(){
  console.log(this.foo);
}
f1();
f1.bind(this);
f1();

let f2 = () => {
  console.log(this.foo)
}
f2();
f2.apply(this);