<?php 

Class Mymodel extends CI_Model{
	function auth($table,$where){
		return $this->db->get_where($table,$where);
	}
}