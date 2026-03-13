;; Traffic Light MM2 / Hyperon Experimental
;; States: Red, Green, Yellow
;; Transition rules (cyclic)

(program Z (state Red))
(program (S Z) (state Green))
(program (S (S Z)) (state Yellow))

;; Rewrite rules: state transitions
(rule transition
  (state Red)    => (state Green))

(rule transition
  (state Green)  => (state Yellow))

(rule transition
  (state Yellow) => (state Red))

;; Executor: run n steps from initial state
(exec_traffic_light (clocked Z steps $n)
  (, (exec_traffic_light (clocked $t steps $n))
     (state $s)
     (transition (state $s) $s_next)
     (steps > 0))
  (, (exec_traffic_light (clocked (S $t) steps (- $n 1))
     (state $s_next))))