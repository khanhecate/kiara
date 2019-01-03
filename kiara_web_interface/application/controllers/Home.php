<?php 
Class Home extends CI_Controller
{
	function __construct(){
		parent::__construct();
		$this->load->model('mymodel');
		
		set_include_path(get_include_path() . PATH_SEPARATOR . APPPATH . 'third_party/phpseclib');
		include(APPPATH . '/third_party/phpseclib/Net/SSH2.php');
		define('NET_SSH2_LOGGING', NET_SSH2_LOG_COMPLEX);

	}
	public function index(){
			if($this->session->userdata('status') != 'login'){
			redirect(base_url('home/auth'));
		}
			$ssh['hostname'] = $this->session->userdata('hostname');
			$ssh['port'] = $this->session->userdata('port');
			$ssh['username'] = $this->session->userdata('username');
			$ssh['password'] = $this->session->userdata('password');
				$ssh_connect = new Net_SSH2($ssh['hostname']);
			if(!$login['connect'] = $ssh_connect->login($ssh['username'],$ssh['password'])){
				$ssh_connect->login($ssh['username'],$ssh['password']);
			}
			if($query = $this->input->post('query')){
				$str = $query;
				echo $ssh_connect->exec($str);
				// $this->load->view('dashboard2',$execute);
				// $this->load->view('result');
				// echo $execute;
			}else{
			$this->load->view('dashboard');
		}
	}
	public function auth(){
		$this->load->view('auth');
	}
	public function do_auth(){
		$hostname = $this->input->post('hostname');
		$port = $this->input->post('port');
		$username = $this->input->post('username');
		$password = $this->input->post('password');
		$active = 1;
		$where = array(
				'username' => $username,
				'password' => md5($password),
				'active' => $active
				);
			$cek = $this->mymodel->auth('user',$where)->num_rows();
		if($cek > 0){
			$data_sesi = array(
					'hostname' => $hostname,
					'port' => $port,
					'username' => $username,
					'password' => $password,
					'status' => 'login',
						);
			$this->session->set_userdata($data_sesi);
			redirect('home/index');
		}else{
			redirect(base_url('home/auth')."?login=false");
		}
	}
		public function ssh_connect(){
			
	}
		public function logout(){
			$this->session->sess_destroy();
			redirect(base_url('home/auth'));
		}
		public function versi(){
			echo phpversion();
		}
}
 ?>