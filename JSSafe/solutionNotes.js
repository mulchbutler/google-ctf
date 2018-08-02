ѐ = function anonymous(x) {
    return window
}
ѡ = function anonymous(x) {
    return x[0] ^ x[1]
}
Ѧ = function anonymous(x) {
    return x[0] | x[1]
}
Ѱ = function anonymous(x) {
    return crypto.subtle.digest(x)
}

ѹ = crypto.subtle.digest('SHA-256', new TextEncoder().encode(password))


solution = [230, 104, 96, 84, 111, 24, 205, 187, 205, 134, 179, 94, 24, 181, 37, 191, 252, 103, 247, 114, 198, 80, 206, 223, 227, 255, 122, 0, 38, 250, 29, 238]