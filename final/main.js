(function () {
    const N = 10
    const M = 37
    const L = 1000000000

    const main = () => {
        for (let i = 0; i < N; i++) {
            console.log(withTime(() => {
                // fib(M)
                addMany(L)
            }))
        }
    }

    const withTime = (fn) => {
        const start = performance.now()
        fn()
        const end = performance.now()
        return end - start
    }

    const fib = n => {
        if (n === 0 || n === 1) {
            return 1
        } else {
            return fib(n - 2) + fib(n - 1)
        }
    }

    const addMany = n => {
        let v = 0
        for (let i = 0; i < n; i++) {
            v = v + 1
        }
    }

    main()
}())

