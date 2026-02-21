<?php
/**
 * 7 Contoh API Sederhana dengan PHP 7
 */

header('Content-Type: application/json');

// ============================================
// 1. API GET - Ambil semua data
// ============================================
function getAllUsers() {
    $users = [
        ['id' => 1, 'name' => 'Andi', 'email' => 'andi@mail.com'],
        ['id' => 2, 'name' => 'Budi', 'email' => 'budi@mail.com'],
        ['id' => 3, 'name' => 'Citra', 'email' => 'citra@mail.com']
    ];
    return json_encode(['status' => 'success', 'data' => $users]);
}

// ============================================
// 2. API GET - Ambil data berdasarkan ID
// ============================================
function getUserById(int $id): string {
    $users = [
        1 => ['id' => 1, 'name' => 'Andi', 'email' => 'andi@mail.com'],
        2 => ['id' => 2, 'name' => 'Budi', 'email' => 'budi@mail.com'],
        3 => ['id' => 3, 'name' => 'Citra', 'email' => 'citra@mail.com']
    ];
    
    if (isset($users[$id])) {
        return json_encode(['status' => 'success', 'data' => $users[$id]]);
    }
    return json_encode(['status' => 'error', 'message' => 'User tidak ditemukan']);
}

// ============================================
// 3. API POST - Tambah data baru
// ============================================
function createUser(array $data): string {
    // Validasi input
    if (empty($data['name']) || empty($data['email'])) {
        return json_encode(['status' => 'error', 'message' => 'Name dan email wajib diisi']);
    }
    
    $newUser = [
        'id' => rand(100, 999),
        'name' => $data['name'],
        'email' => $data['email']
    ];
    
    return json_encode(['status' => 'success', 'message' => 'User berhasil dibuat', 'data' => $newUser]);
}

// ============================================
// 4. API PUT - Update data
// ============================================
function updateUser(int $id, array $data): string {
    if (empty($data['name']) && empty($data['email'])) {
        return json_encode(['status' => 'error', 'message' => 'Tidak ada data untuk diupdate']);
    }
    
    $updatedUser = [
        'id' => $id,
        'name' => $data['name'] ?? 'Unknown',
        'email' => $data['email'] ?? 'unknown@mail.com'
    ];
    
    return json_encode(['status' => 'success', 'message' => 'User berhasil diupdate', 'data' => $updatedUser]);
}

// ============================================
// 5. API DELETE - Hapus data
// ============================================
function deleteUser(int $id): string {
    if ($id <= 0) {
        return json_encode(['status' => 'error', 'message' => 'ID tidak valid']);
    }
    return json_encode(['status' => 'success', 'message' => "User dengan ID $id berhasil dihapus"]);
}

// ============================================
// 6. API Search - Cari data
// ============================================
function searchUsers(string $keyword): string {
    $users = [
        ['id' => 1, 'name' => 'Andi Pratama', 'email' => 'andi@mail.com'],
        ['id' => 2, 'name' => 'Budi Santoso', 'email' => 'budi@mail.com'],
        ['id' => 3, 'name' => 'Citra Dewi', 'email' => 'citra@mail.com'],
        ['id' => 4, 'name' => 'Andi Wijaya', 'email' => 'andi.w@mail.com']
    ];
    
    $results = array_filter($users, function($user) use ($keyword) {
        return stripos($user['name'], $keyword) !== false || 
               stripos($user['email'], $keyword) !== false;
    });
    
    return json_encode(['status' => 'success', 'count' => count($results), 'data' => array_values($results)]);
}

// ============================================
// 7. API dengan Authentication sederhana
// ============================================
function authenticatedEndpoint(string $token): string {
    $validToken = 'secret123';
    
    if ($token !== $validToken) {
        http_response_code(401);
        return json_encode(['status' => 'error', 'message' => 'Unauthorized - Token tidak valid']);
    }
    
    return json_encode([
        'status' => 'success', 
        'message' => 'Authenticated!',
        'data' => ['secret' => 'Data rahasia hanya untuk user terautentikasi']
    ]);
}

// ============================================
// Router sederhana
// ============================================
$method = $_SERVER['REQUEST_METHOD'];
$action = $_GET['action'] ?? '';
$id = isset($_GET['id']) ? (int)$_GET['id'] : 0;

switch ($action) {
    case 'users':
        if ($method === 'GET' && $id > 0) {
            echo getUserById($id);
        } elseif ($method === 'GET') {
            echo getAllUsers();
        } elseif ($method === 'POST') {
            $data = json_decode(file_get_contents('php://input'), true) ?? $_POST;
            echo createUser($data);
        } elseif ($method === 'PUT') {
            $data = json_decode(file_get_contents('php://input'), true);
            echo updateUser($id, $data);
        } elseif ($method === 'DELETE') {
            echo deleteUser($id);
        }
        break;
        
    case 'search':
        $keyword = $_GET['q'] ?? '';
        echo searchUsers($keyword);
        break;
        
    case 'protected':
        $token = $_SERVER['HTTP_AUTHORIZATION'] ?? $_GET['token'] ?? '';
        $token = str_replace('Bearer ', '', $token);
        echo authenticatedEndpoint($token);
        break;
        
    default:
        echo json_encode([
            'status' => 'info',
            'message' => 'API Sederhana PHP 7',
            'endpoints' => [
                'GET  ?action=users' => 'Ambil semua users',
                'GET  ?action=users&id=1' => 'Ambil user by ID',
                'POST ?action=users' => 'Tambah user baru',
                'PUT  ?action=users&id=1' => 'Update user',
                'DELETE ?action=users&id=1' => 'Hapus user',
                'GET  ?action=search&q=andi' => 'Cari user',
                'GET  ?action=protected&token=secret123' => 'Endpoint terproteksi'
            ]
        ]);
}
