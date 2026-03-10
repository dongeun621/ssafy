// 1. if 조건문
let num = 10;

if (num >= 10) {
  console.log("num은 10 이상입니다");
} else if (num >= 5) {
  console.log("num은 5 이상입니다");
} else {
  console.log("거짓입니다");
}

// 2. switch
// 다수의 조건

let animal = "cat";

switch (animal) {
  case "cat": {
    console.log("고양이");
    break; //break안하면 고양이가 만족하면 그 밑에도 다 출력됨
  }
  case "dog": {
    console.log("개");
    break;
  }
  case "bear": {
    console.log("곰");
    break;
  }
  default: {
    console.log("동물 x");
  }
}
