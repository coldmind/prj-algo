(defun get-string-hash (string)
  (let ((hash 7))
    (loop for char across string do
	 (setf hash (+ (* hash 31) (char-code char))))
    (return-from get-string-hash hash)))


(defun make-table (size)
  (make-array size :initial-element '()))


(defun insert-val (table key value)
  (let ((hash (mod (get-string-hash key) (length table))))
    ;; Check if key is already in the table
    (if (aref table hash)
	(if (string= (car (aref table hash)) key)
	    (return-from insert-val -1)))
    (let ((value-been-set nil))
      ;; We need to look from current position
      ;; to the end of the table.
      ;; If we can not insert a key, do the same from
      ;; the beginning of the table.
      (loop for i from hash to (- (length table) 1) do
	   (if (not (aref table i))
	       (progn
		 (setf (aref table i) (list key value))
		 (setf value-been-set t)
		 (return))))
      (if (not value-been-set)
	  (loop for i from 0 to hash do
	       (if (not (aref table i))
		   (progn
		     (setf (aref table i) (list key value))
		     (setf value-been-set t)
		     (return)))))
      ;; Table is full, need to extend it.
      (if (not value-been-set)
	  (print "hashtable is full, need to extend it")))))
		 

(defun get-val (table key)
  (let ((hash (mod (get-string-hash key) (length table))))
    (if (aref table hash)
	(if (string= (car (aref table hash)) key)
	    (return-from get-val (cdr (aref table hash)))))
    (loop for i from hash to (- (length table) 1) do
	 (if (aref table i)
	     (if (string= (car (aref table i)) key)
		 (return-from get-val (cdr (aref table i))))))
    (loop for i from 0 to hash do
	 (if (aref table i)
	     (if (string= (car (aref table i)) key)
		 (return-from get-val (cdr (aref table i))))))
    (return-from get-val -1)))
