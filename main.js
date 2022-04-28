


var affine = {
    "a":0,
    "b":1,
    "c":2,
    "d":3,
    "e":4,
    "f":5,
    "g":6,
    "h":7,
    "i":8,
    "j":9,
    "k":10,
    "l":11,
    "m":12,
    "n":13,
    "o":14,
    "p":15,
    "q":16,
    "r":17,
    "s":18,
    "t":19,
    "u":20,
    "v":21,
    "w":22,
    "x":23,
    "y":24,
    "z":25,
}

function gcd(x, y) {
    if ((typeof x !== 'number') || (typeof y !== 'number')) 
    return false;
  x = Math.abs(x);
  y = Math.abs(y);
  while(y) {
    var t = y;
    y = x % y;
    x = t;
  }
  return x;
}



function print(s) {
    console.log(s);
}

affine_key_list = Object.keys(affine);
affine_value_list = Object.values(affine);

print(affine_key_list);
print(affine_value_list);


function encrypt(s, a, b) {
    s=s.toLowerCase();
    if (gcd(a, 26)!=1) {
        print("ERROR, Alpha isn't coprime with 26");
        return false;
    }
    else {
        enc=[];
        str=s.split("");
        for (i=0; i<26; i=i+1) {
            num=affine[str[i]];
            newnum=(a*num+b) % 26;
            enc.push(affine_key_list[newnum])
        }
        return enc.join("");
    }
}

function decrypt(s, a, b) {
    s=s.toLowerCase();
    if (gcd(a, 26)!=1) {
        print("ERROR, Alpha isn't coprime with 26");
        return false;
    }
    else {
        ainv = 0;
        enc=[];
        str=s.split("");
        for (x=0; x<26; x=x+1) {
            if ((a*x) % 26 == 1) {
                ainv=x;
                break;
            }
        }
        for (i=0; i<26; i=i+1) {
            num=affine[str[i]];
            newnum=(ainv*(num-b)) % 26;
            enc.push(affine_key_list[newnum])
        }
        return enc.join("");
    }
}

print(encrypt("hi", 5, 8));
print(decrypt("rw", 5, 8));