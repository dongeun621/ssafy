// 1. 객체 생성
let obj1 = new Object(); //객체 생성자
let obj2 = {}; //객체 리터럴(대부분사용)

// 2. 객체 프로퍼티(객체 속성)
let person = {
  name: "이동은",
  age: 27,
  hobby: "테니스",
  a: {},
  b: function () {},
  c: true,
  "like cat": true, //띄어쓰기 있으면 key에 띄어쓰기
};

// 3. 객체 프로퍼티를 다루는 방법
// 3.1 특정 프로퍼티에 접근 (점 표기법, 괄호 표기법)
let name = person.name;
console.log(name);
let age = person["age"];

let property = "hobby";
let hobby = person[property];

//3.1 새로운 프로퍼티 추가방법, 수정도 동일
person.job = "developer";
person["favoriteFood"] = "떡볶이";

//3.2 프로퍼티 삭제
delete person.job;
delete person["favoriteFood"];

//3.3 프로퍼티 존재 유무(in 연산자)
let result1 = "name" in person;
