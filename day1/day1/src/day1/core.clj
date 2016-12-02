(ns day1.core
  (:gen-class))

(require '[clojure.string :as string])

(def instructions "L5, R1, R4, L5, L4, R3, R1, L1, R4, R5, L1, L3, R4, L2, L4, R2, L4, L1, R3, R1, R1, L1, R1, L5, R5, R2, L5, R2, R1, L2, L4, L4, R191, R2, R5, R1, L1, L2, R5, L2, L3, R4, L1, L1, R1, R50, L1, R1, R76, R5, R4, R2, L5, L3, L5, R2, R1, L1, R2, L3, R4, R2, L1, L1, R4, L1, L1, R185, R1, L5, L4, L5, L3, R2, R3, R1, L5, R1, L3, L2, L2, R5, L1, L1, L3, R1, R4, L2, L1, L1, L3, L4, R5, L2, R3, R5, R1, L4, R5, L3, R3, R3, R1, R1, R5, R2, L2, R5, L5, L4, R4, R3, R5, R1, L3, R1, L2, L2, R3, R4, L1, R4, L1, R4, R3, L1, L4, L1, L5, L2, R2, L1, R1, L5, L3, R4, L1, R5, L5, L5, L1, L3, R1, R5, L2, L4, L5, L1, L1, L2, R5, R5, L4, R3, L2, L1, L3, L4, L5, L5, L2, R4, R3, L5, R4, R2, R1, L5")

(defn abs [n] (max n (- n)))
(defn sum [lst] (reduce + lst))

(defn split-instruction [i]
  [(nth (seq i) 0), (read-string (apply str (rest (seq i))))]
)

(defn turn-left [d]
  (mod (- d 1) 4)
  )

(defn turn-right [d]
  (mod (+ d 1) 4)
  )

(defn dir-from-pts [p1 p2]
  (if (= (nth p1 0) (nth p2 0))
    (let [dy (- (nth p2 1) (nth p1 1))]
      (if (< dy 0) 3 1)
      )
    (let [dx (- (nth p2 0) (nth p1 0))]
      (if (< dx 0) 2 0)
      )
    )
  )

(defn do-move [prevsteps move]
  (let [
         facing (if (< (count prevsteps) 2) 0 (apply dir-from-pts (take-last 2 prevsteps)))
         pos (last prevsteps)
         dist (last move)
         turn (first move)
         ]

    (let [newdir (if (= turn \R) (turn-right facing) (turn-left facing))]
      (concat prevsteps
        (case newdir
          0 (map (fn [x] [(+ (nth pos 0) (+ x 1)) (nth pos 1)]) (range dist))
          1 (map (fn [y] [(nth pos 0) (+ (nth pos 1) (+ y 1))]) (range dist))
          2 (map (fn [x] [(- (nth pos 0) (+ x 1)) (nth pos 1)]) (range dist))
          3 (map (fn [y] [(nth pos 0) (- (nth pos 1) (+ y 1))]) (range dist))
          )
        )
      )
    )
  )

(defn find-first-dupe [points]
  (first (filter (fn [p] (> (count (filter (fn [p2] (= p p2)) points)) 1)) points))
  )

(defn -main
 [& args]
  (let [all-points (reduce do-move [[0 0]] (map split-instruction (string/split instructions #", ")))]
    (println (str "Part 1 Location: " (last all-points)))
    (println (str "Part 1 Distance: " (sum (map abs (last all-points)))))
    (let [actual (find-first-dupe all-points)]
      (println (str "Part 2 Location: " actual))
      (println (str "Part 2 Distance: " (sum (map abs actual))))
      )
    )
)
