// 1. 묵시적 형 변환
// -> 자바스크립트 엔진이 알아서 형 변환 하는 것

let num = 10;
let str = "20";

const result = num + str; //1020

// 2. 암시적 형 변환
// -> 프로그래머 내장함수 등을 이용해서 직접 형 변환

let strl = "10";
let strToNum1 = Number(strl);

// 문자열 -> 숫자
let str2 = "10개"; // 숫자가 앞쪽에 있어야됨
let strToNum2 = parseInt(str2);

// 숫자 -> 문자열
let num1 = 20;
let numToStrl = String(num1);
console.log(numToStrl + "입니다");
